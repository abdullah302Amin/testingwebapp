using System.Web.Mvc;

namespace SimpleWebApp.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            ViewBag.Message = "Welcome to the Simple ASP.NET Web App!";
            return View();
        }
    }
}
