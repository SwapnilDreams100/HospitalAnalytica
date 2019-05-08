base_url = "http://127.0.0.1:5000/";

function q1(){
  $.ajax({
          type: "GET",
          async:false,
          url: base_url + "q1",
          dataType: "json",
          success: function(result) {
            console.log(result)
            bar_chart('1', "ENCOUNTER vs YEAR",'year','encounter_count',result)
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}

function q2(disease_name){
  $.ajax({
          type: "GET",
          url: base_url + "q2",
          asyn:false,
          data:{
            "disease":disease_name
          },
          dataType: "json",
          success: function(result) {
            
            line_chart('2', "MEDICINE-Cost vs YEAR: "+ disease_name,'year','Cost',result)
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}
function q6(cond_name){
  $.ajax({
          type: "GET",
          url: base_url + "q6",
          asyn:false,
          data:{
            "condition":cond_name
          },
          dataType: "json",
          success: function(result) {
            
            pie_chart('6', "Disease-Male vs Female: "+ cond_name,result)
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}

function q_maps(){
$.ajax({
          type: "GET",
          url: base_url + "maps",
          asyn:false,
          dataType: "json",
          success: function(result) {
            console.log(result)
          maps(result)
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });
}
function q5(proc_name){
  $.ajax({
          type: "GET",
          url: base_url + "q5",
          asyn:false,
          data:{
            "procedure":proc_name
          },
          dataType: "json",
          success: function(result) {
            
            line_chart('5', "Operation-Cost vs YEAR: "+ proc_name,'year','Cost',result)
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}

function q_medic(){
  $.ajax({
          type: "GET",
          url: base_url + "q_medic",
          async:false,
          dataType: "json",
          success: function(result) {
            string_total= ''
            for(var i=0; i<result.length;i++){

              string_op='<option name="choice'+i+'" value="'+result[i]+'" >'+result[i]+'</option>';
              string_total+=string_op;
            }
            $('#medic_choice_div').html(string_total);
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}

function q_proc(){
  $.ajax({
          type: "GET",
          url: base_url + "q_proc",
          async:false,
          dataType: "json",
          success: function(result) {
            string_total= ''
            for(var i=0; i<result.length;i++){
              string_op='<option name="choice'+i+'" value="'+result[i]+'" >'+result[i]+'</option>';
              string_total+=string_op;
            }
            $('#proce_choice_div').html(string_total);
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}

function q_cond(){
  $.ajax({
          type: "GET",
          url: base_url + "q_cond",
          async:false,
          dataType: "json",
          success: function(result) {
            string_total= ''
            for(var i=0; i<result.length;i++){
              string_op='<option name="choice'+i+'" value="'+result[i]+'" >'+result[i]+'</option>';
              string_total+=string_op;
            }
            $('#condi_choice_div').html(string_total);
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}

function q3(){
  $.ajax({
          type: "GET",
          url: base_url + "q3",
          async:false,
          dataType: "json",
          success: function(result) {
            console.log(result)
            bar_chart('3', "Utilization vs Hospital: ",'Org','Util',result)
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}

function q4(){
  $.ajax({
          type: "GET",
          url: base_url + "q4",
          async:false,
          dataType: "json",
          success: function(result) {
            
            bar_chart('4', "Condition vs Time: ",'Diseases','Average Duration',result)
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
                  alert("Some error occured in get file, Try Again");
          },
        });  
}


// function q_count_org(State){
//   $.ajax({
//           type: "GET",
//           url: base_url + "q5",
//           data:{
//             "State":State
//           },
//           dataType: "json",
//           success: function(result) {
            
//             bar_chart('5', "Organisation vs State: ",'Count of Organisation','State',result)
//           },
//           error: function(XMLHttpRequest, textStatus, errorThrown){
//                   alert("Some error occured in get file, Try Again");
//           },
//         });  
// }

// function q_count(){
//   $.ajax({
//           type: "GET",
//           url: base_url + "q_count",
//           dataType: "json",
//           success: function(result) {
//             string_total= ''
//             for(var i=0; i<result.length;i++){
//                   // naveen add one correct dropdown item here you meana mediation yes
//               string_op=' <option name="choice'+i+'" value="'+result[i]+'" >'+result[i]+'</option>';
//               string_total+=string_op;
//             }
//             console.log(string_total)
//             $('#count_org').html(string_total);
//           },
//           error: function(XMLHttpRequest, textStatus, errorThrown){
//                   alert("Some error occured in get file, Try Again");
//           },
//         });  
// }


// function feedback(email, fb){
//   $.ajax({
//           type: "POST",
//           url: base_url + "feedback",
//           data:{
//             "email":email,
//             "feedback":fb,
//           },
//           dataType: "json",
//           success: function(result) {
//                     alert('Successfully recorded')
                  
//           },
//           error: function(XMLHttpRequest, textStatus, errorThrown){
//                   alert("Some error occured, Try Again");
//           },
//           beforeSend: function(){
//                   $loading_img.show();
//           },
//           complete: function(){
//                   $loading_img.hide();

//           }
//         });  