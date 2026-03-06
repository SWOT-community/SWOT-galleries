document.addEventListener("DOMContentLoaded", async () => {
  try {
    const downloadLink = document.querySelector(".admonition.note a.download");
    if (!downloadLink) return;

    const currentFile = downloadLink.getAttribute("href"); 
    const notebookName = currentFile.replace(".ipynb", "");
    console.log(notebookName);

    const response = await fetch("../_static/notebook_versions.json");
    if (!response.ok) return;

    const data = await response.json();
    const nbData = data[notebookName];
    if (!nbData || !nbData.versions) return;
    console.log(nbData.versions);

    const sortedVersions = nbData.versions.sort((a, b) =>
      new Date(b.date) - new Date(a.date)
    );

    const previousVersions = sortedVersions.slice(1);
    console.log(previousVersions);
    if (previousVersions.length === 0) return;

    const container = document.querySelector(".other-versions-container");
    if (!container) return;

    const title = document.createElement("h4");
    title.textContent = "Previous versions:";
    container.appendChild(title);

    const ul = document.createElement("ul");
    ul.className = "previous-versions";

    previousVersions.forEach(v => {
      const li = document.createElement("li");
      const a = document.createElement("a");

      a.href = v.file + "?raw=true";
      a.textContent = `${v.date} (${v.commit})`;
      a.setAttribute("download", getFilename(v.file));
      li.appendChild(a);

      if (v.message) {
        const span = document.createElement("span");
        span.textContent = ` — ${v.message}`;
        li.appendChild(span);
      }

      ul.appendChild(li);
    });

    container.appendChild(ul);

    function getFilename(pathOrUrl) {
      return pathOrUrl.split("/").pop();
    }

  } catch (err) {
    console.warn("Erreur lors du remplissage des anciennes versions :", err);
  }
});
