import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyDnNVGBKUHh_wQT7GmELb1ye5G4eW-Fmms",
  authDomain: "ijmch-bf355.firebaseapp.com",
  projectId: "ijmch-bf355",
  storageBucket: "ijmch-bf355.appspot.com",
  messagingSenderId: "218231333552",
  appId: "1:218231333552:web:36e96d80aad616c97f1175",
  measurementId: "G-FRLL9JT2ER"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
