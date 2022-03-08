var clear_btns = document.getElementsByClassName("clear-btn");

if (clear_btns != null) {

    for(var i = 0; i < clear_btns.length; i++){

        clear_btns[i].addEventListener("click", function () {

            id = this.dataset.id
            action = this.dataset.action
            type = this.dataset.type

            if (user_is_staff) {
                console.log("ACTION:", action, "TYPE:", type);
                clear_user_order(action, type);
            } else {
                console.log("User is not staff");
            }
          });
    }
}

function clear_user_order(action, type) {
  var url = "/csv_orders/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ action: action, item_type: type }),
  })
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      location.reload();
      console.log("DATA:", data);
    });
}
