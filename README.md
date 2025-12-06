
TCP Client-Server Communication using Python (Socket Programming)

This project demonstrates how two devices communicate over a network using **TCP sockets**.
It includes:

* A **TCP Server** that supports multiple clients using **threads**
* A **TCP Client** for two-way message exchange
* Proper connection handling and safe termination

Socket programming is a fundamental skill in networking and cybersecurity, where reliable and ordered communication is required.

---

🔹 What is a Socket?

A socket is a virtual connection point for communication between two applications in a network.
Just like a phone call connects two phones, a socket connects two programs to exchange data.

---

🚀 Features

✔ Bidirectional communication (Send & Receive messages)
✔ Multiple client connections using threading
✔ Graceful exit by typing `"exit"`
✔ Simple & beginner-friendly Python implementation

---

 🔧 Tools & Technologies

| Tool/Technology               | Purpose                   |
| ----------------------------- | ------------------------- |
| Python                        | Implementation language   |
| Socket Library                | Creating TCP connection   |
| Threading                     | Handling multiple clients |
| Windows PowerShell / Terminal | Executing scripts         |

---

 📌 Project Structure

```
📁 TCP-Socket-Project
 ├── server.py
 ├── client.py
 ├── README.md  (this file)
```

---

 🖥 Source Code

🔹 Server Code

Handles multiple client connections using threads
→ Source: https://github.com/zinannalakath15/Socket_TCP_Communication/blob/main/server.py

🔹 Client Code

Connects to server and exchanges messages
→ Source: https://github.com/zinannalakath15/Socket_TCP_Communication/blob/main/client.py

---

📡 How It Works (Flow)

1️⃣ Run the server → It listens on `127.0.0.1:9753`
2️⃣ One or more clients connect
3️⃣ Clients send messages → Server responds back
4️⃣ When `"exit"` is sent → Connection closes

---

 🔒 Cybersecurity Use Cases

*(Based on explanation from PDF)* 

| Application         | How TCP Sockets Are Used         |
| ------------------- | -------------------------------- |
| Port Scanning       | Find open network ports          |
| SSH / Remote Access | Secure command execution         |
| Network Monitoring  | Capture & inspect traffic        |
| Ethical Hacking     | Simulate attacks & communication |

Understanding socket communication is essential for network security professionals.

---

 ▶️ How to Run

 Start Server

```bash
python server.py
```

 Start Client (Open multiple terminals)

```bash
python client.py
```

---

 📈 Future Improvements

*(Mentioned in documentation)* 

* Add encryption for secure message transfer
* Create a GUI-based chat application
* Store chat logs for monitoring

---

 👨‍💻 Author

**N K Muhammed Zinan**
Cyber Security – Week 16 Project



