/* ==========================
   TYPEWRITER EFFECT
========================== */

var app = document.getElementById("typing");

if (app) {

    var title = app.dataset.title || "Python Developer";

    var typewriter = new Typewriter(app, {
        loop: true,
        delay: 70,
        deleteSpeed: 40
    });

    typewriter
        .typeString(title)
        .pauseFor(1500)
        .deleteAll()
        .typeString("Django Developer")
        .pauseFor(1500)
        .deleteAll()
        .typeString("Frontend Developer")
        .pauseFor(1500)
        .start();
}


/* ==========================
   AOS ANIMATION
========================== */

if (typeof AOS !== "undefined") {

    AOS.init({
        duration: 1000,
        once: true
    });

}


/* ==========================
   SCROLL TO TOP BUTTON
========================== */

const topBtn = document.getElementById("topBtn");

window.addEventListener("scroll", function () {

    if (!topBtn) return;

    if (window.scrollY > 300) {

        topBtn.style.display = "block";

    } else {

        topBtn.style.display = "none";

    }

});


if (topBtn) {

    topBtn.addEventListener("click", function () {

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });

}


/* ==========================
   ACTIVE NAVBAR
========================== */

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".menu a");

window.addEventListener("scroll", function () {

    let current = "";

    sections.forEach(function (section) {

        const sectionTop =
            section.offsetTop - 120;

        if (window.scrollY >= sectionTop) {

            current =
                section.getAttribute("id");

        }

    });


    navLinks.forEach(function (link) {

        link.classList.remove("active");

        if (
            link.getAttribute("href") ===
            "#" + current
        ) {

            link.classList.add("active");

        }

    });

});


/* ==========================
   DARK / LIGHT MODE
========================== */

const themeBtn =
    document.getElementById("themeBtn");

if (themeBtn) {

    themeBtn.addEventListener("click", function () {

        document.body.classList.toggle(
            "light-mode"
        );

    });

}


/* =====================================================
   AMAR SHAHARE | DEVELOPER BOOT LOADER
===================================================== */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const loader =
            document.getElementById(
                "developer-loader"
            );

        if (!loader) return;


        const terminalOutput =
            document.getElementById(
                "terminal-output"
            );

        const activeCommand =
            document.getElementById(
                "active-command"
            );

        const progressBar =
            document.getElementById(
                "progress-bar"
            );

        const progressPercent =
            document.getElementById(
                "progress-percent"
            );

        const progressStage =
            document.getElementById(
                "progress-stage"
            );

        const bootStatus =
            document.getElementById(
                "boot-status-text"
            );

        const systemReady =
            document.getElementById(
                "system-ready"
            );

        const architectureNodes =
            document.querySelectorAll(
                ".architecture-node"
            );


        /* ==========================
           BOOT LOG
        ========================== */

        const bootLines = [

            {
                text:
                    "Loading portfolio environment...",
                stage:
                    "INITIALIZING SYSTEM",
                progress: 12
            },

            {
                text:
                    "Python runtime initialized",
                stage:
                    "STARTING PYTHON RUNTIME",
                progress: 25
            },

            {
                text:
                    "Django framework connected",
                stage:
                    "CONNECTING DJANGO",
                progress: 40
            },

            {
                text:
                    "Loading database configuration",
                stage:
                    "LOADING DATABASE",
                progress: 55
            },

            {
                text:
                    "Fetching portfolio data",
                stage:
                    "FETCHING PORTFOLIO DATA",
                progress: 68
            },

            {
                text:
                    "Initializing frontend interface",
                stage:
                    "INITIALIZING FRONTEND",
                progress: 82
            },

            {
                text:
                    "Optimizing developer experience",
                stage:
                    "OPTIMIZING INTERFACE",
                progress: 93
            },

            {
                text:
                    "All systems operational",
                stage:
                    "FINALIZING SYSTEM",
                progress: 100
            }

        ];


        /* ==========================
           TERMINAL LINE
        ========================== */

        function addTerminalLine(
            message,
            success = false
        ) {

            if (!terminalOutput) return;

            const line =
                document.createElement("div");

            line.className =
                "terminal-line";

            line.innerHTML = `
                <span class="prompt">&gt;</span>
                ${message}
                ${
                    success
                        ? '<span class="success"> [OK]</span>'
                        : ''
                }
            `;

            terminalOutput.appendChild(line);

            terminalOutput.scrollTop =
                terminalOutput.scrollHeight;

        }


        /* ==========================
           ARCHITECTURE
        ========================== */

        function activateArchitecture(
            progress
        ) {

            if (!architectureNodes.length)
                return;

            let activeCount = 1;

            if (progress >= 40)
                activeCount = 2;

            if (progress >= 55)
                activeCount = 3;

            if (progress >= 82)
                activeCount = 4;


            architectureNodes.forEach(
                function (node, index) {

                    if (index < activeCount) {

                        node.classList.add(
                            "active"
                        );

                    } else {

                        node.classList.remove(
                            "active"
                        );

                    }

                }
            );

        }


        /* ==========================
           UPDATE PROGRESS
        ========================== */

        function updateProgress(
            value,
            stage
        ) {

            if (progressBar) {

                progressBar.style.width =
                    value + "%";

            }


            if (progressPercent) {

                progressPercent.textContent =
                    String(value)
                        .padStart(2, "0") + "%";

            }


            if (progressStage) {

                progressStage.textContent =
                    stage;

            }


            activateArchitecture(
                value
            );

        }


        /* ==========================
           TYPE ACTIVE COMMAND
        ========================== */

        function typeCommand(
            text,
            callback
        ) {

            if (!activeCommand) {

                if (callback)
                    callback();

                return;
            }


            activeCommand.textContent = "";

            let index = 0;

            const typingSpeed = 22;

            const typing =
                setInterval(
                    function () {

                        activeCommand.textContent =
                            text.substring(
                                0,
                                index
                            );

                        index++;


                        if (
                            index >
                            text.length
                        ) {

                            clearInterval(
                                typing
                            );

                            if (callback)
                                callback();

                        }

                    },
                    typingSpeed
                );

        }


        /* ==========================
           BOOT SEQUENCE
        ========================== */

        let currentLine = 0;


        function runBootSequence() {

            if (
                currentLine >=
                bootLines.length
            ) {

                finishBoot();

                return;
            }


            const line =
                bootLines[currentLine];


            if (bootStatus) {

                bootStatus.textContent =
                    line.stage;

            }


            typeCommand(
                line.text,
                function () {

                    addTerminalLine(
                        line.text,
                        true
                    );


                    updateProgress(
                        line.progress,
                        line.stage
                    );


                    currentLine++;


                    setTimeout(
                        runBootSequence,
                        330
                    );

                }
            );

        }


        /* ==========================
           FINISH BOOT
        ========================== */

        function finishBoot() {

            if (bootStatus) {

                bootStatus.textContent =
                    "ONLINE";

            }


            if (activeCommand) {

                activeCommand.textContent =
                    "system.ready()";

            }


            updateProgress(
                100,
                "SYSTEM READY"
            );


            if (systemReady) {

                systemReady.classList.add(
                    "show"
                );

            }


            setTimeout(
                function () {

                    loader.classList.add(
                        "loader-hidden"
                    );


                    setTimeout(
                        function () {

                            loader.style.display =
                                "none";


                            /* ==================
                               NORMAL VERTICAL SCROLL
                            ================== */

                            document.body.style.overflowX =
                                "hidden";

                            document.body.style.overflowY =
                                "auto";

                        },
                        750
                    );

                },
                700
            );

        }


        /* ==========================
           START LOADER
        ========================== */

        /*
         * Disable scrolling only
         * while the boot loader is visible.
         */

        document.body.style.overflow =
            "hidden";


        updateProgress(
            0,
            "SYSTEM INITIALIZATION"
        );


        setTimeout(
            runBootSequence,
            500
        );

    }
);

/* ==========================
   DJANGO MESSAGE AUTO HIDE
========================== */

document.addEventListener("DOMContentLoaded", function () {

    const djangoMessages =
        document.querySelectorAll(".django-message");

    djangoMessages.forEach(function (message) {

        setTimeout(function () {

            message.style.transition =
                "opacity 0.5s ease, transform 0.5s ease";

            message.style.opacity = "0";
            message.style.transform = "translateX(30px)";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 4000);

    });

});