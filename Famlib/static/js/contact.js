function changeSectionTitle(value) {
    const sectionTitle = document.getElementById("section-title");
    if (value === "feedback") {
      sectionTitle.textContent = "Got a suggestion or feedback? We're all ears! Fill out the form and let us know what's on your mind";
    } else {
      sectionTitle.textContent = "Let's stay connected! Send us a message and we'll get back to you as soon as possible.";
    }
}