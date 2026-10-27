
document.addEventListener("DOMContentLoaded", function () {

    // VM status chart
    const chartElement = document.getElementById("vmChart");

    if (chartElement) {

        new Chart(chartElement, {
            type: "doughnut",

            data: {
                labels: ["Running", "Stopped"],

                datasets: [{
                    data: [runningVMs, stoppedVMs],
                    backgroundColor: ["#22c55e", "#f97316"],
                    borderWidth: 0,
                    hoverOffset: 8
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false,

                plugins: {
                    legend: {
                        position: "bottom",
                        labels: {
                            padding: 20,
                            usePointStyle: true
                        }
                    }
                },

                cutout: "70%"
            }
        });
    }

});


// Confirm before deleting a VM
function confirmDelete(vmId, vmName) {

    const confirmed = confirm(
        "Are you sure you want to delete " + vmName + "?"
    );

    if (confirmed) {
        window.location.href = "/delete/" + vmId;
    }
}