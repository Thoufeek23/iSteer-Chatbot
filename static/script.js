document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("chat-form");
  const chatBox = document.getElementById("chat-box");
  const input = document.getElementById("user-input");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const message = input.value.trim();
    if (!message) return;

    addMessage("user", message);
    input.value = "";

    const typingIndicator = addTypingIndicator();

    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
      });

      typingIndicator.remove();

      if (!response.ok) throw new Error("Network error");

      const data = await response.json();
      const cleanedResponse = data.response.replace(/in the provided text/gi, "");
      addMessage("bot", cleanedResponse);
    } catch (err) {
      typingIndicator.remove();
      addMessage("bot", "Sorry, I'm having trouble connecting. Please try again.");
      console.error(err);
    }
  });

  function addMessage(sender, text) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerHTML = formatMessage(text);
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  function formatMessage(text) {
    if (text.includes("<button")) {
    return text;
  }
    let formatted = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    formatted = formatted.replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank">$1</a>');
    return formatted
      .split("\n")
      .map(line => line.trim().startsWith("* ") ? `<div class="bullet-point">• ${line.slice(2)}</div>` : line)
      .join("<br>");
  }

  function addTypingIndicator() {
    const indicator = document.createElement("div");
    indicator.classList.add("message", "bot");
    indicator.innerHTML = `
      <div class="typing-indicator">
        <span>Thinking</span>
        <span class="dots">
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
        </span>
      </div>
    `;
    chatBox.appendChild(indicator);
    chatBox.scrollTop = chatBox.scrollHeight;
    return indicator;
  }

  input.focus();
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      form.dispatchEvent(new Event("submit"));
    }
  });
});
