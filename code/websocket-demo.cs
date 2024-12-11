using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using (ClientWebSocket webSocket = new ClientWebSocket())
        {
            Uri serverUri = new Uri("wss://example.com/socket"); // Replace with your WebSocket server URI

            try
            {
                Console.WriteLine("Connecting to WebSocket...");
                await webSocket.ConnectAsync(serverUri, CancellationToken.None);
                Console.WriteLine("Connected!");

                // Sending a message
                string messageToSend = "Hello, WebSocket!";
                byte[] messageBytes = Encoding.UTF8.GetBytes(messageToSend);
                await webSocket.SendAsync(new ArraySegment<byte>(messageBytes), WebSocketMessageType.Text, true, CancellationToken.None);
                Console.WriteLine($"Sent: {messageToSend}");

                // Receiving a message
                byte[] buffer = new byte[1024];
                WebSocketReceiveResult result = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);
                string messageReceived = Encoding.UTF8.GetString(buffer, 0, result.Count);
                Console.WriteLine($"Received: {messageReceived}");

                // Closing the WebSocket
                Console.WriteLine("Closing WebSocket...");
                await webSocket.CloseAsync(WebSocketCloseStatus.NormalClosure, "Goodbye", CancellationToken.None);
                Console.WriteLine("WebSocket closed.");
            }
            catch (WebSocketException ex)
            {
                Console.WriteLine($"WebSocket error: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Unexpected error: {ex.Message}");
            }
        }
    }
}