var clear_btn = document.getElementById("clear-btn")
var sor_items = document.getElementsByClassName("update-csv-queue")

if (clear_btn != null){

    clear_btn.addEventListener("click", function() {

        for (var i = 0; i < sor_items.length; i++) {
        
            sor = sor_items[i]
            sor_id = sor.dataset.sor;
            action = sor.dataset.action;
        
            if (user_is_staff) {
                console.log("SOR ID: ", sor_id, "ACTION: ", action);
                update_user_order(sor_id, action);
            } else {
                console.log("User is not staff");
            }
        }
    })
}


function update_user_order(sor_id, action) {
  var url = "/sor_entry/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ sor_id: sor_id, action: action }),
  })
    .then((response) => {
        return response.json();
    })

    .then((data) => {
        location.reload()
        console.log("DATA:", data);
    });
}