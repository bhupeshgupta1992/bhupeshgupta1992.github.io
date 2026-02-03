import { auth, db, storage } from "./firebase-config.js";
import { collection, addDoc } 
from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
import { ref, uploadBytes, getDownloadURL } 
from "https://www.gstatic.com/firebasejs/10.12.0/firebase-storage.js";
import { onAuthStateChanged } 
from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

let currentUser = null;

onAuthStateChanged(auth, (user) => {
  currentUser = user;
});

const submitBtn = document.getElementById("submitBtn");

submitBtn.addEventListener("click", async () => {

  if (!currentUser) {
    alert("Please login first");
    return;
  }

  const title = document.getElementById("title").value;
  const abstract = document.getElementById("abstract").value;
  const file = document.getElementById("file").files[0];

  if (!title || !abstract || !file) {
    alert("Fill all fields");
    return;
  }

  try {
    const storageRef = ref(storage, "manuscripts/" + Date.now() + "_" + file.name);
    await uploadBytes(storageRef, file);
    const fileURL = await getDownloadURL(storageRef);

    await addDoc(collection(db, "submissions"), {
      title,
      abstract,
      authorEmail: currentUser.email,
      fileURL,
      status: "Submitted",
      createdAt: new Date()
    });

    alert("Manuscript submitted successfully");
    window.location.href = "dashboard.html";

  } catch (error) {
    alert(error.message);
  }
});
