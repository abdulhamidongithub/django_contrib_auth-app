// to identifikatsiya ----------------------------------
function identifikatsiya(){
    let login = document.getElementById('login').value
    let password = document.getElementById('password').value

//    if(login === "mendau" && password === '12345678'){
//        location.href = "/bulimlar.html"
//    }else {
//        alert('Login yoki parol xato kiritildi!!!')
//    }
}

// to open new Product Modal ----------------------------------
$(document).ready(function(){
    $("#newProduct").click(function(){
      $("#newProductModal").modal({backdrop: "static"});
    });
    $("#newClient").click(function(){
        $("#newClientModal").modal({backdrop: "static"});
    });
    $(".edit-client").click(function(){
        $("#editClientModal").modal({backdrop: "static"});
    });
    $(".edit-product").click(function(){
        $("#editProductModal").modal({backdrop: "static"});
    });
    
});

// Set parametrs for Edit---------------------------------------
function editClient(client){
    document.getElementById('edit-client-name').value = client.name
    document.getElementById('edit-client-shop').value = client.shop
    document.getElementById('edit-client-number').value = client.number
    document.getElementById('edit-client-location').value = client.location
}
function editProduct(product){
    document.getElementById('edit-product-name').value = product.name
    document.getElementById('edit-product-brend').value = product.brend
    document.getElementById('edit-product-price').value = product.price
    document.getElementById('edit-product-amount').value = product.amount
}

