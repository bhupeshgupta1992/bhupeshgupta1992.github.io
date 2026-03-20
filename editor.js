import { db } from "./firebase-config.js";
import { collection, getDocs, doc, updateDoc } 
from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

const container = document.getElementById("editorList");

async function loadSubmissions() {

  const snapshot = await getDocs(collection(db, "submissions"));

  container.innerHTML = "";

  snapshot.forEach(d => {

    const data = d.data();

    container.innerHTML += `
      <div class="card p-3 mb-3">
        <h5>${data.title}</h5>
        <p><strong>Author:</strong> ${data.authorEmail}</p>
        <p><strong>Status:</strong> ${data.status}</p>

        <a href="${data.fileURL}" target="_blank" class="btn btn-sm btn-dark mb-2">
          Download Manuscript
        </a>

        <div>
          <button class="btn btn-sm btn-warning" onclick="updateStatus('${d.id}','Under Review')">
            Under Review
          </button>

          <button class="btn btn-sm btn-success" onclick="updateStatus('${d.id}','Accepted')">
            Accept
          </button>

          <button class="btn btn-sm btn-danger" onclick="updateStatus('${d.id}','Rejected')">
            Reject
          </button>
        </div>

      </div>
    `;
  });

}

window.updateStatus = async function(id, status) {

  const refDoc = doc(db, "submissions", id);

  await updateDoc(refDoc, {
    status: status
  });

  alert("Status updated to " + status);

  loadSubmissions();
}

loadSubmissions();
