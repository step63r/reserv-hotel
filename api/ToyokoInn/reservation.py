import datetime
import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from ..service_definitions import ReservationBase
import process_format
import site_config


class ToyokoInnReservation(ReservationBase):
    def __init__(self, process_format: process_format.ProcessFormat, login_info: process_format.LoginInfo):
        self._chrome_options = webdriver.ChromeOptions()
        self._chrome_options.add_argument('--headless')
        self._chrome_options.add_argument('--no-sandbox')
        self._chrome_options.add_argument('--disable-dev-shm-usage')
        self._driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=self._chrome_options)
        self._process_format = process_format
        self._login_info = login_info

    def execute(self) -> bool:
        ret = False
        logging.info('処理を開始しました')
        logging.info(f"> ホテルID　　：{self._process_format.hotel.hotel_id}")
        logging.info(f"> チェックイン：{datetime.datetime.strftime(self._process_format.checkin_date, '%Y/%m/%d')}")

        logging.debug('ドライバ初期化中')
        self._message = 'ドライバ初期化中'

        # 仮想画面サイズ設定
        self._driver.set_window_size(1920, 1080)
        
        # アクセス
        self._message = 'アクセス中'
        logging.debug(f"アクセス中：{site_config.BASE_URL}")
        self._driver.get(site_config.BASE_URL)
        
        # キャンセルチェック
        if self._check_cancel():
            logging.debug('キャンセルされました')
            self._message = 'キャンセルされました'
            return ret

        # 詳細ページへ
        logging.debug(f"詳細ページへ移動中：{site_config.BASE_URL}search/detal/{self._process_format.hotel.hotel_id}")
        self._message = '詳細ページへ移動中'
        self._driver.get(f"{site_config.BASE_URL}search/detal/{self._process_format.hotel.hotel_id}")

        # キャンセルチェック
        if self._check_cancel():
            logging.debug('キャンセルされました')
            self._message = 'キャンセルされました'
            return ret

        try:
            self._count += 1
            logging.debug('--------------------------------------------------')
            logging.debug(f"継続回数：{self._count}")

            # 予約ページへ
            logging.debug(f"予約ページへ移動中：{site_config.BASE_URL}search/reserve/room?chckn_date={datetime.datetime.strftime(self._process_format.checkin_date, '%Y/%m/%d')}&room_type={str(self._process_format.type.room_type_id)}")
            self._message = '予約ページへ移動中'
            self._driver.get(f"{site_config.BASE_URL}search/reserve/room?chckn_date={datetime.datetime.strftime(self._process_format.checkin_date, '%Y/%m/%d')}&room_type={str(self._process_format.type.room_type_id)}")

            # キャンセルチェック
            if self._check_cancel():
                logging.debug('キャンセルされました')
                self._message = 'キャンセルされました'
                return ret
            
            # 禁煙・喫煙による分岐
            if not self._process_format.enable_no_smoking and not self._process_format.enable_smoking:
                # 禁煙・喫煙両方0だった場合、エラー
                pass
            elif self._process_format.enable_no_smoking and self._process_format._enable_smoking:
                # 禁煙・喫煙両方1だった場合
                if not self._process_format.smoking_first:
                    # 禁煙を優先
                    ret = self._search_room('禁煙', self._process_format.strict_room_type, self._process_format.type.room_type_name)
                    if ret:
                        logging.debug('禁煙　空室あり')
                        self._message = '禁煙　空室あり'
                    else:
                        logging.debug('満室')
                        self._message = '満室'
                else:
                    # 喫煙を優先
                    ret = self._search_room('喫煙', self._process_format.strict_room_type, self._process_format.type.room_type_name)
                    if ret:
                        logging.debug('喫煙　空室あり')
                        self._message = '喫煙　空室あり'
                    else:
                        ret = self._search_room('禁煙', self._process_format.strict_room_type, self._process_format.type.room_type_name)
                        if ret:
                            logging.debug('禁煙　空室あり')
                            self._message = '禁煙　空室あり'
                        else:
                            logging.debug('満室')
                            self._message = '満室'
            elif self._process_format.enable_no_smoking:
                ret = self._search_room('禁煙', self._process_format.strict_room_type, self._process_format.type.room_type_name)
                if ret:
                    logging.debug('禁煙　空室あり')
                    self._message = '禁煙　空室あり'
                else:
                    logging.debug('禁煙　満室')
                    self._message = '禁煙　満室'
            else:
                ret = self._search_room('喫煙', self._process_format.strict_room_type, self._process_format.type.room_type_name)
                if ret:
                    logging.debug('喫煙　空室あり')
                    self._message = '喫煙　空室あり'
                else:
                    logging.debug('喫煙　満室')
                    self._message = '喫煙　満室'
            
            # キャンセルチェック
            if self._check_cancel():
                logging.debug('キャンセルされました')
                self._message = 'キャンセルされました'
                return ret
        
            # ログイン試行
            if not self._try_login():
                logging.fatal('ログインに失敗')
                logging.info('このエラーは自動リトライできません')
                self._message = 'ログインに失敗'
                return ret
            
            # 空室発見～予約確定
            if ret:
                logging.debug('予約中')
                self._message = '予約中'
                # 電話番号入力
                logging.debug(f"処理中：{site_config.XPATH_TEL}")
                self._driver.find_element(By.XPATH, site_config.XPATH_TEL).send_keys(self._login_info.login_tel)
                # チェックイン予定時刻
                logging.debug(f"処理中：{site_config.XPATH_CHKINTIME}")
                chktime_element = self._driver.find_element(By.XPATH, site_config.XPATH_CHKINTIME)
                chktime_select_element = Select(chktime_element)
                chktime_select_element.select_by_value(self._process_format.checkin_value.checkin_value)
                # 確認ボタン押下
                logging.debug(f"処理中：{site_config.XPATH_CONFIRM}")
                self._driver.find_element(By.XPATH, site_config.XPATH_CONFIRM).click()

                # 同一日で予約があった場合
                try:
                    # Waitオブジェクトを定義
                    wait = WebDriverWait(self._driver, 3)

                    # iframeに操作をスイッチ
                    wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, site_config.IFRAME_OVERWRITE)))
                    logging.debug(f"処理中：{site_config.XPATH_OVERWRITE}")
                    if self._driver.find_element(By.XPATH, site_config.XPATH_OVERWRITE).text == site_config.STR_OVERWRITE:
                        if self._process_format._enable_overwrite:
                            self._driver.find_element(By.XPATH, site_config.XPATH_BTN_OVERWRITE).click()
                        else:
                            # raise
                            pass
                except NoSuchElementException:
                    # 何もしない
                    pass
                except WebDriverException:
                    # 何もしない
                    pass
            
            # 予約＆正常終了確認
            try:
                # チェックボックスにチェック
                logging.debug(f"処理中：{site_config.XPATH_CHKAGREE}")
                self._driver.find_element(By.XPATH, site_config.XPATH_CHKAGREE).click()

                # 確定ボタン押下
                logging.debug(f"処理中：{site_config.XPATH_OK}")
                self._driver.find_element(By.XPATH, site_config.XPATH_OK).click()

                logging.debug(f"処理中：{site_config.XPATH_CHK_VALIDATE}")
                str_chk = self._driver.find_element(By.XPATH, site_config.XPATH_CHK_VALIDATE).text

                if not str_chk == site_config.STR_VALIDATE:
                    # 要素はあるが文字が違う
                    logging.debug('予約できませんでした（文字列が異なります）')
                    self._message = '予約できませんでした'
                    ret = False
                    if self._process_format.enable_auto_retry:
                        # TODO: 処理をキャンセルしない
                        logging.info('処理を続行します')
                    else:
                        return ret
                    
            except NoSuchElementException:
                # 要素がない
                logging.debug('予約できませんでした（要素が存在しません）')
                self._message = '予約できませんでした'
                ret = False
                if self._process_format.enable_auto_retry:
                    # TODO: 処理をキャンセルしない
                    logging.info('処理を続行します')
                else:
                    return ret
            
            if ret:
                logging.debug('予約完了')
                self._message = '予約完了'

        except Exception as e:
            logging.error(e.with_traceback())
            if self._process_format.enable_auto_retry:
                # TODO: 処理をキャンセルしない
                pass
            else:
                # TODO: 処理をキャンセルする
                pass

        return ret
    
    def _try_login(self) -> bool:
        """
        ログインを試みる

        Returns
        -------
        bool
            ログイン成否（既にログイン済の場合は True を返す）
        """
        ret = False
        logging.info('ログイン中')
        self._message = 'ログイン中'
        try:
            logging.debug(f"処理中：{site_config.XPATH_FORM_ADDRESS}")
            self._driver.find_element(By.XPATH, site_config.XPATH_FORM_ADDRESS).send_keys(self._login_info.login_address)
            logging.debug(f"処理中：{site_config.XPATH_PASS}")
            # TODO: KeyVaultあたりで暗号化
            self._driver.find_element(By.XPATH, site_config.XPATH_PASS).send_keys(self._login_info.login_pass)
            logging.debug(f"処理中：{site_config.XPATH_PASS}")
            self._driver.find_element(By.XPATH, site_config.XPATH_LOGINBTN).click()

            # ログイン失敗
            if self._driver.current_url == f"{site_config.BASE_URL}login":
                pass
            else:
                ret = True

        except NoSuchElementException:
            # ログイン不要
            ret = True
        
        return ret

    def _check_cancel(self) -> bool:
        """
        キャンセルチェック

        Returns
        -------
        bool
            キャンセルされた場合True
        """
        ret = False
        # TODO: キャンセル処理
        return ret
    
    def _search_room(self, match: str, strict_room_type: bool, room_type_name: str) -> bool:
        """
        空き部屋を検索する

        Parameters
        ----------
        match : str
            禁煙、もしくは喫煙
        strict_room_type : bool
            厳密な部屋タイプのみに限定する
        room_type_name : str
            部屋タイプ名

        Returns
        -------
        bool
            指定条件で空き部屋が見つかった場合True
        """
        ret = False
        i = 1

        while True:
            try:
                # 禁煙・喫煙のラベルを取得
                element = self._driver.find_element(By.XPATH, site_config.XPATH_SMOKELABEL.replace('INTEGER', str(i))).text
                if (element == match):
                    try:
                        if strict_room_type:
                            room_name = self._driver.find_element(By.XPATH, site_config.XPATH_ROOM_NAME.replace('INTEGER', str(i))).text.replace(f"{match }", '')
                            # 厳密な部屋タイプ名称と不一致であればカウンタを回して続行
                            if room_name != room_type_name:
                                i += 1
                                continue

                        self._driver.find_element(By.XPATH, site_config.XPATH_RESERVEBTN.replace('INTEGER', str(i))).click()
                        # 予約ボタンが押下可能な状態だったらループを抜ける
                        ret = True
                        break
                    
                    except NoSuchElementException:
                        # カウンタを回して続行
                        i += 1
                        continue
                else:
                    # カウンタを回して続行
                    i += 1
                    continue


            except NoSuchElementException:
                # 要素がもうない
                break
        
        return ret
