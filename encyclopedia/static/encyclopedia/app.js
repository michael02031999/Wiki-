let alert_notification = document.getElementById(
  "alert_notification"
);

console.log(alert_notification.innerHTML.length);

if (alert_notification.innerHTML.length == 8) {
  alert_notification.style.padding = 0;
  alert_notification.style.margin = 0;
  alert_notification.style.border = "none";
}
