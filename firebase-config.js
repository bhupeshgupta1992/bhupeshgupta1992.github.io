// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDnNVGBKUHh_wQT7GmELb1ye5G4eW-Fmms",
  authDomain: "ijmch-bf355.firebaseapp.com",
  projectId: "ijmch-bf355",
  storageBucket: "ijmch-bf355.firebasestorage.app",
  messagingSenderId: "218231333552",
  appId: "1:218231333552:web:36e96d80aad616c97f1175",
  measurementId: "G-FRLL9JT2ER"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
