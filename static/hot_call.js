$(document).ready(function () {
    $.getJSON('/api/hotcall', function (data) {
      var htm = `<table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">S.No.</th>
          
          <th scope="col">Customer Name</th>
          <th scope="col">Caller Id</th>
          <th scope="col">Status</th>
          <th scope="col">Caller Name</th>
          <th scope="col">Current Date</th>
          <th scope="col">Phone Status</th>
          <th scope="col"> Conversation</th>
          <th scope="col"> Leadstatus</th>
          <th scope="col"> Mobile</th>
        </tr>
      </thead>
     <tbody>`
     
      data.map((item) => {
        htm += `<tr>
  <th th scope = "row" > ${item.id}</th> 
       
  <td>${item.customername} </td>
  <td>${item.callerid}</td>       
  <td>${item.status}</td>       
  <td>${item.callername}</td>       
  <td>${item.currentdate}</td>       
  <td>${item.phonestatus}</td>       
  <td>${item.conversation}</td>       
  <td>${item.leadstatus}</td>       
  <td>${item.mobileno}</td>       `
      })
  
      htm += `</tbody ></table > `
      $('#HotData').html(htm)
  
    })
  })
  
  