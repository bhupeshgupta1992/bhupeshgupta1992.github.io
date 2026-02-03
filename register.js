import { auth } from "./firebase-config.js";
import { createUserWithEmailAndPassword } 
from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

const registerBtn = document.getElementById("registerBtn");

registerBtn.addEventListener("click", async () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    await createUserWithEmailAndPassword(auth, email, password);
    alert("Registration successful");
    window.location.href = "login.html";
  } catch (error) {
    alert(error.message);
  }
});
