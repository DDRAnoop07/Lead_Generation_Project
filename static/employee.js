$(document).ready(function() {
    $.getJSON("/api/employeelist", function(data) {
        var htm = `<table class="table table-hover">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Birth</th>
        <th scope="col">Contact</br>Details</th>
        <th scope="col">Address</th>
        <th scope="col">Designation</th>
        <th scope="col">Manager</th>
        <th scope="col">Picture</th>
        <th scope="col">Update</th>
      </tr>
    </thead>
    <tbody>`;
        data.map((item) => {
            htm += `<tr>
  <th scope="row">${item.id}</th>
  <td>${item.firstname} ${item.lastname}</ td>
  <td>${item.gender}<br>${item.dob}</ td>
  <td>${item.emailid}<br>${item.mobileno}</ td>
  <td>${item.address}<br>${item.cityname},${item.statename}</ td>
  <td>${item.designation}</ td>
  <td>${item.mfirstname} ${item.mlastname}</ td>
  <td><a href='/api/display_employee_picture?employeeid=${item.id}&employeename=${item.firstname} ${item.lastname}&picture=${item.photograph}'><img src="/${item.photograph}" width="30"></a></ td>
  <td><a href='/api/employeebyid?employeeid=${item.id}'>Update/Delete</a></td>`;
        });
        htm += `</tbody></table>`;
        $("#employeeData").html(htm);
    });
});