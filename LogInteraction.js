import React, { useState } from "react";
import axios from "axios";

export default function LogInteraction() {
  const [msg, setMsg] = useState("");
  const [response, setResponse] = useState("");

  const send = async () => {
    const res = await axios.post("http://127.0.0.1:8000/chat", {
      message: msg,
    });
    setResponse(JSON.stringify(res.data));
  };

  return (
    <div>
      <h2>AI CRM Chat</h2>
      <input value={msg} onChange={(e) => setMsg(e.target.value)} />
      <button onClick={send}>Send</button>
      <pre>{response}</pre>
    </div>
  );
}