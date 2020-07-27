/*

LINKS IN JAVASCRIPT FOR ADMIN SIDE
Made By
24 Ave Pizza

*/

//QrCode
function enterQrCode() {
    location.replace("/qr-code")
}

function enterGenQrCode() {
    location.replace("/qr-code-gen/")
}

function enterDeleteQrCode(id) {
    location.replace("/delete-qrcode/" + id)
}


//Password Tracker
function enterPasswordTracker() {
    location.replace("/password-tracker")
}


//Filemanager
function enterFilemanager() {
    location.replace("/filemanager")
}


//Edit menu
function enterEditMenu() {
    location.replace("/edit-menu")
}

function enterTableMenuAdmin() {
    location.replace("/view-tables-menu-admin")
}

function enterAddMenu(id) {
    location.replace("/add-menu/" + id)
}


function enterDeleteMenu(id, path) {
    location.replace("/delete-menu/" + id + path);
}


//Edit Client
function enterEditclient() {
    location.replace("/edit-client")
}


function enterAddClient(id) {
    location.replace("/add-client/" + id)
}


function enterDeleteClient(id) {
    location.replace("/delete-client/" + id)
}


//About Us Admin
function enterAboutUsAdminin() {
    location.replace("/edit-about")
}


//Dashboard (Offers)
function enterOffersDashboard() {
    location.replace("/dashboard")
}

function enterEditOffers(id) {
    location.replace("/edit/" + id)
}

function enterDeleteOffers(id) {
    location.replace("/delete/" + id)
}


//Admin Contact Us
function enterAdminContactUs() {
    location.replace("/contactus-admin")
}

function enterAdminContactUsView(id) {
    location.replace("/view-contactus-admin/" + id)
}

function enterAdminContactUsMail(id) {
    location.replace("/mail-contactus-admin/" + id)
}

function enterAdminContactUsDelete(id) {
    location.replace("/delete-contactus-admin/" + id)
}


//LogOut
function enterLogout() {
    location.replace("/logout")
}