using System;

namespace SimpleWebApp
{
    public partial class _Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }

        protected void btnClickMe_Click(object sender, EventArgs e)
        {
            lblMessage.Text = "Button clicked at " + DateTime.Now.ToString();
        }
    }
}
