var update_btns = document.getElementsByClassName("update-csv-queue");

for (var i = 0; i < update_btns.length; i++) {
  update_btns[i].addEventListener("click", function () {
    var sor_id = this.dataset.sor;
    var action = this.dataset.action;

    console.log("SOR ID: ", sor_id, "ACTION: ", action);

    if (user_is_staff) {
      update_user_order(sor_id, action);
    } else {
      console.log("User is not staff");
    }
  });
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