$(() => {
    $("#consultBtn").click(e =>{
        e.preventDefault();
        msg = "Reserve a date with the Boss by sending your request to our official email address. \n You will be hearing from one of our management team"

        alert(msg)
    })

    $("#educationBtn").click( e => {
        e.preventDefault()
        let phone = prompt("Enter your phone number")
        let endPoint = `${location.href}service/edu/`
        
    });
})