fetch("images.json")
  .then(response => response.json())
  .then(images => {
      const gallery = document.getElementById("gallery");
      images.forEach(img => {
          let imageElement = document.createElement("img");
          imageElement.src = img;
          gallery.appendChild(imageElement);
      });
  })
  .catch(error => console.error("Error loading images:", error));
