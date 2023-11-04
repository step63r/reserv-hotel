using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace MinatoProject.ReservHotel.Functions
{
    public static class HttpTrigger1
    {
        [FunctionName("HttpTrigger1")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", "post", Route = null)] HttpRequest req,
            ILogger log)
        {
            var results = new Data[] {
                new() { Id = 1, Name = "Sato" },
                new() { Id = 2, Name = "Suzuki" },
            };

            return new JsonResult(results);
        }
    }

    public class Data
    {
        public int Id{ get; set; }
        public string Name{ get; set; }
    }
}
