
const clubsData = [
    {
        name: "GDSC",
        description: "Technical Club",
        activities: ["Seminar on IOT at 5pm "],
    },
    {
        name: "SI Crew",
        description: "dancing club",
        activities: ["Practice Session at 7pm"],
    },
    // Add more club data objects as needed
];

// Function to dynamically populate clubs section
function populateClubsSection() {
    const clubsSection = document.getElementById("clubs");

    clubsData.forEach((club) => {
        const clubDiv = document.createElement("div");
        clubDiv.classList.add("club");

        clubDiv.innerHTML = `
            <h2>${club.name}</h2>
            <p>${club.description}</p>
            <ul class="activities">
                ${club.activities.map((activity) => `<li>${activity}</li>`).join("")}
            </ul>
        `;

        clubsSection.appendChild(clubDiv);
    });
}


populateClubsSection();
