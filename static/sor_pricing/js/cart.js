var update_btns = document.getElementsByClassName("update-csv-queue");
var url = "/csv_orders/update_item/";

for (var i = 0; i < update_btns.length; i++) {
  update_btns[i].addEventListener("click", function () {
    var id = this.dataset.id;
    var action = this.dataset.action;
    var type = this.dataset.type

    console.log("ID: ", id, "ACTION: ", action, 'TYPE: ', type);

    if (user_is_staff) {
      update_user_order(id, action, type);
    } else {
      console.log("User is not staff");
    }
  });
}

function update_user_order(id, action, type) {

  fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ item_id: id, action: action, item_type: type}),
  })
    .then((response) => {
        return response.json();
    })

    .then((data) => {
        location.reload()
        console.log("DATA:", data);
    });
}