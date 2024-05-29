using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string url = "https://mixed-reality-apis-zvglklnxya-em.a.run.app/create";
        string email = "example@example.com";
        var payload = new { email };

        using (HttpClient client = new HttpClient())
        {
            try
            {
                HttpResponseMessage response = await client.PostAsJsonAsync(url, payload);
                if (response.IsSuccessStatusCode)
                {
                    Console.WriteLine("User created successfully");
                }
                else
                {
                    Console.WriteLine($"Failed to create user: {response.Content.ReadAsStringAsync().Result}");
                }
            }
            catch (HttpRequestException e)
            {
                Console.WriteLine($"Failed to create user: {e.Message}");
            }
        }
    }
}