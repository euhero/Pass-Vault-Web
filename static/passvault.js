


function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
	}
async function changebutton(){
  await sleep(1000);
  document.getElementById('genpass').setAttribute("data-clipboard-text", makeid(12));
  document.getElementById('genpass').innerHTML = 'Generate Decoy Password'
  document.getElementById('genpass').setAttribute('class','btn btn-lg btn-primary btn-block')

	}

function showorhidepass(){
  var x = document.getElementById('password');
  var y = document.getElementById('eye');
  if (x.type === 'password'){
	  x.type = 'text';
	  y.setAttribute('class','fa fa-eye-slash')
  } else {
	  
	  x.type = 'password'
	  y.setAttribute('class','fa fa-eye')
	  
  		}
}