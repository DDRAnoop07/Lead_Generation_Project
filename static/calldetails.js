$(document).ready(function(){

    $.getJSON('/api/calldetailslist',function(data){
        //   console.log("calldetailslist:",data)
          table(data)
      })    
    
      $('#to').change(function(){
        $.getJSON('/api/calldetails_list_by_date',{from: $('#from').val(),to:$('#to').val()},function(data){
            table(data)
        })
    })
  
    $('#leadstatus').change(function(){
        if($(this).val()=='Hot')
        { 
            $.getJSON('/api/calldetails_list_by_LeadStatus',{leadstatus:$('#leadstatus').val()},
            function(data){
                table(data)
                
            })
        
        }
        else if($(this).val()=='Warm')
        {
            $.getJSON('/api/calldetails_list_by_LeadStatus',{leadstatus:$('#leadstatus').val()},
            function(data){
                table(data)
            })
        }
        else if($(this).val()=='Cold')
        {
            $.getJSON('/api/calldetails_list_by_LeadStatus',{leadstatus:$('#leadstatus').val()},
            function(data){
                table(data)
                
            })
        }
        else if($(this).val()=='Freeze')
        {
            $.getJSON('/api/calldetails_list_by_LeadStatus',{leadstatus:$('#leadstatus').val()},
            function(data){
                table(data)
                
            })
        }
    })
  
    $('#phonestatus').change(function(){
        if($(this).val()=='Connected')
        {
           $.getJSON('/api/calldetails_list_by_PhoneStatus',{phonestatus:$('#phonestatus').val()},
           function(data){
            table(data)
           })
        }
        else if($(this).val()=='Not Connected')
        {
            $.getJSON('/api/calldetails_list_by_PhoneStatus',{phonestatus:$('#phonestatus').val()},
            function(data){
             table(data)
            })
        }
        
    })
     
  function table(data) {
    var htm=`<table class="table table-hover">
    <thead>
      <tr>
        <th scope="col">S.No.</th>
        <th scope="col">Name</th>
        <th scope="col">caller</th>
        <th scope="col">Date</th>
        <th scope="col">Phonestatus</th>
        <th scope="col">Conversation</th>
        <th scope="col">leadstatus</th>
        <th scope="col">Mobileno</th>
      </tr>
    </thead>
    <tbody>`
    
    data.map((item)=>{
        htm+= `<tr>
        <th scope="row">${item.id}</th>
        <td>${item.customername}</td>
        <td>${item.callerid}  ${item.status}<br>${item.callername}</td>
        <td>${item.currentdate}</td>
        <td>${item.phonestatus}</td>
        <td>${item.conversation}</td>
        <td>${item.leadstatus}</td>
        <td>${item.mobileno}</td>
        `
    })
  
    htm+=`</tbody> </table>`
  
    $('#calldetailsData').html(htm)
  
  }  
  
      
  })
  
  
 
  