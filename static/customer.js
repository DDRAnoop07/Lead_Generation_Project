$(document).ready(function() {
    $.getJSON('/api/customerlist', function(data) {
        var htm = `<table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Birth</th>
          <th scope="col">Contact Details</th>
          <th scope="col">Address</th>
          <th scope="col">Organization Name</th>
          <th scope="col">Picture</th>
          <th scope="col">Make Call</th>
          <th scope="col">Follow Up</th>
          <th scope="col">Update</th>
        </tr>
      </thead>
      <tbody>`

        data.map((item) => {
            htm += `<tr>
  <th th scope = "row" > ${item.id} </th> 
  <td>${item.firstname} ${item.lastname}</td>   
  <td>${item.dob}</td>           
  <td>${item.emailid} <br>${item.mobileno} <br>${item.alternateno}</td>       
  <td>${item.address} <br>${item.cityname}<br>${item.statename}</td>   
  <td>${item.organizationname} </td>           
  <td><a href='/api/customerdisplaypicture?customerid=${item.id}&customername=${item.firstname} ${item.lastname}&picture=${item.photograph}'><img src="/${item.photograph}" width="30"></a></ td>
  <td><a href="tel:${item.mobileno}">Call</a></td>
  <td> <a href = '/api/callcustomerbyid?customerid=${item.id}'>Fill Detail</a></td>
  <td> <a href = '/api/customerbyid?customerid=${item.id}'>Update/Delete</a></td >`;

        })

        htm += ` </tbody ></table > `
        $('#customerData').html(htm)

    })
})