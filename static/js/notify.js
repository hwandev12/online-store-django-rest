var notify_badge_class;
var notify_menu_class;
var notify_api_url;
var notify_fetch_count;
var notify_unread_url;
var notify_mark_all_unread_url;
var notify_refresh_period = 2000;
// Set notify_mark_as_read to true to mark notifications as read when fetched
var notify_mark_as_read = false;
var consecutive_misfires = 0;
var registered_functions = [];

let notifyTable = document.querySelector(".datas");


function fill_notification_badge(data) {
  var badges = document.getElementsByClassName(notify_badge_class);
  if (badges) {
    for (var i = 0; i < badges.length; i++) {
      badges[i].innerHTML = data.unread_count;
    }
  }
}

function fill_notification_list(data) {
  var menus = document.getElementsByClassName(notify_menu_class);
  if (menus) {
    var messages = data.unread_list
      .map(function (item) {
        var message = "";

        if (typeof item.actor !== "undefined") {
          message = '<td>' + item.actor + '<td/>';
        }
        // if (typeof item.verb !== "undefined") {
        //   message = message + '<td>' + item.verb + '<td/>';
        // }
        if (typeof item.target !== "undefined") {
          message = message + " " + item.target;
        }
        // if (typeof item.timestamp !== "undefined") {
        //   message = message + " " + item.timestamp;
        // }
        let d = new Date(item.timestamp);
        return `<a style='text-decoration: none !important;' href='/mark-as-read/${item.slug}/'>
          <li style='list-style: none;' class='list-group-item position-relative'>
            ${message}
            <p style='display: inline-block; position: absolute; right: 50%;'>${d.getDate()}.${d.getDay()}<sup>${d.getHours()}:${d.getMinutes()}</sup></p>
            <i class="fa-solid fa-envelope position-absolute" style="color: orange; font-size: 20px; right: 20px;"></i>
          </li>
        </a>`;
      })
      .join("");

    for (var i = 0; i < menus.length; i++) {
      menus[i].innerHTML = messages;
    }
  }
}

function register_notifier(func) {
  registered_functions.push(func);
}

function fetch_api_data() {
  // only fetch data if a function is setup
  if (registered_functions.length > 0) {
    var r = new XMLHttpRequest();
    var params = "?max=" + notify_fetch_count;

    if (notify_mark_as_read) {
      params += "&mark_as_read=true";
    }

    r.addEventListener("readystatechange", function (event) {
      if (this.readyState === 4) {
        if (this.status === 200) {
          consecutive_misfires = 0;
          var data = JSON.parse(r.responseText);
          for (var i = 0; i < registered_functions.length; i++) {
            registered_functions[i](data);
          }
        } else {
          consecutive_misfires++;
        }
      }
    });
    r.open("GET", notify_api_url + params, true);
    r.send();
  }
  if (consecutive_misfires < 10) {
    setTimeout(fetch_api_data, notify_refresh_period);
  } else {
    var badges = document.getElementsByClassName(notify_badge_class);
    if (badges) {
      for (var i = 0; i < badges.length; i++) {
        badges[i].innerHTML = "!";
        badges[i].title = "Connection lost!";
      }
    }
  }
}


function my_special_notification_callback(data) {
  for (var i=0; i < data.unread_list.length; i++) {
      msg = data.unread_list[i];
      console.log(msg);
  }
}

setTimeout(fetch_api_data, 1000);
