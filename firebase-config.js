import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-analytics.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyDnvNGBKUH_wQT7GmELb1ye5G4eW-Fmns",
  authDomain: "ijmch-bf355.firebaseapp.com",
  projectId: "ijmch-bf355",
  storageBucket: "ijmch-bf355.appspot.com",
  messagingSenderId: "218231333552",
  appId: "1:218231333552:web:30e96d80aad616c97f1175",
  measurementId: "G-FRLL9JT2ER"
};

const app = initializeApp(firebaseConfig);
getAnalytics(app);

const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);

export { auth, db, storage };
