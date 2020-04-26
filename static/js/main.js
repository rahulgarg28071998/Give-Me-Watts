// alert()
// setTimeout(() => {
//     swal({
//         title: "Good job!",
//         text: "Aaeeee Dael...",
//         icon: "success",
//         button: "Dael",
//     })
//     .then(
//         ()=>alert()
//     );
// }, 3000);

window.onload = () => {
    localStorage. clear();
    var speak;
    setTimeout(() => {
        var clearInt = setInterval(() => {
            $.get("https://api.thingspeak.com/channels/977873/feeds.json?api_key=NPOFZ0FPNJL2U40R&results=1", function(resp){
                var resp = resp.feeds[0];
                var entry_id = resp.entry_id;
                var rf_id = resp.field1;
                var percentage = resp.field2;
                console.log(rf_id);
                if (rf_id != 0){
                    localStorage.setItem("entry_id",entry_id);
                    localStorage.setItem("rf_id",rf_id);
                    localStorage.setItem("percentage",percentage);
                    var speak = `Your current battery percentage: ${percentage}. It will take ${(100-localStorage.getItem("percentage"))*1.4} minutes to charge.`;
                    responsiveVoice.speak(speak,"UK English Male");
                    clearInterval(clearInt);
                    swal({
                        title: `Welcome to the Charging Station`,
                        text: `Your current battery percentage: ${percentage}. It will take ${(100-localStorage.getItem("percentage"))*1.4} minutes to charge.`,
                        icon: "success",
                        button: "Go Ahead",
                    }).then(
                        ()=>window.location = "/recommendation"
                    )
                }
            });
        }, 3000);
    }, 3000);
}