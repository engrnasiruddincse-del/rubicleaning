document.addEventListener("DOMContentLoaded", function () {
    // Use a more robust selector that works with Django admin
    const quoteRequestSelect = document.querySelector("#id_quote_request");
    
    if (quoteRequestSelect) {
        quoteRequestSelect.addEventListener("change", function () {
            const requestId = this.value;
            if (!requestId) {
                // Clear fields if no request is selected
                document.getElementById("id_city").value = "";
                document.getElementById("id_postal_code").value = "";
                document.getElementById("id_address").value = "";
                return;
            }
            
            // Use the full URL
            fetch(`/get-quote-request/${requestId}/`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Check if data exists and populate fields
                    document.getElementById("id_city").value = data.city || "";
                    document.getElementById("id_postal_code").value = data.postal_code || "";
                    document.getElementById("id_address").value = data.address || "";
                })
                .catch(err => {
                    console.error("Error fetching QuoteRequest data:", err);
                    // Clear fields on error
                    document.getElementById("id_city").value = "";
                    document.getElementById("id_postal_code").value = "";
                    document.getElementById("id_address").value = "";
                });
        });
        
        // Trigger the change event on page load if a quote request is already selected
        if (quoteRequestSelect.value) {
            quoteRequestSelect.dispatchEvent(new Event('change'));
        }
    }
});



