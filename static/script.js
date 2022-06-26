function klik(event) {
    if (klavesy.includes(event.key)) {
        if (ukazatel == delkaTextu - 1) {
            document.removeEventListener('keydown', klik);
            document.getElementById("p" + ukazatel).classList.remove("podtrzenePismeno");
            var scripts = document.getElementsByTagName('script');
            window.location.href = "/update/" + scripts[scripts.length - 1].getAttribute("pismena");
        } else {
            const element = document.getElementById("p" + ukazatel);

            if (event.key == element.innerHTML || (event.key == " " && element.innerHTML == "&nbsp;")) {
                if (element.classList.contains("spatnePismeno")){
                    element.classList.remove("spatnePismeno");
                    element.classList.add("opravenePismeno");
                };
                element.classList.remove("podtrzenePismeno");
                ukazatel++;
                document.getElementById("p" + ukazatel).classList.add("podtrzenePismeno");
            } else {
                element.classList.add("spatnePismeno");
            };
        };
    };
}

document.addEventListener('keydown', klik);

let kontejner = document.getElementById("textKontejner")
const klavesy = "abcdefghijklmnopqrstuvwxyzěščřžýáíéúů ";
let ukazatel = 0;
let delkaTextu = document.getElementById("text").getAttribute("data-length");

