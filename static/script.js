async function sendMessage() {
  const input = document.querySelector("#user-input");
  const chatBox = document.querySelector("#chat-box");
  const userMessage = input.value.trim();

  if (!userMessage) return;

  // Display user's message
  chatBox.innerHTML += `<div><strong>You:</strong> ${userMessage}</div>`;
  // console.log(userMessage);
  
  // Send request to backend
  const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage }),
  });

  const data = await response.json();
  // console.log(data);
  
  // Display bot response
  chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;

  // Clear input
  input.value = "";
}

document.addEventListener("DOMContentLoaded", () => {
  const inputBox = document.querySelector("#user-input");
  const sendButton = document.querySelector("#send-button");

  inputBox.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  });

  sendButton.addEventListener("click", sendMessage);
});