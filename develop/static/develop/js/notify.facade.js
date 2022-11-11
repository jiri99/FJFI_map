function notifyMessage(type, message) {

    let iconName = "fa-check";

    if (type === "danger" || type === "warning") {
        iconName = "fa-exclamation";
    } else if (type === "info") {
        iconName = "fa-info";
    }

    $.notify({
        icon: "fa " + iconName,
        message: message
    }, {
        type: type,
        placement: {
            from: 'top',
            align: 'right'
        }
    });

}