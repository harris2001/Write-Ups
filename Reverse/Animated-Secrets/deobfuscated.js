function anonymous() {
    function is_valid_password(pass) {
            //Must be a string of digits[0-9]
            if (!pass.match(/\d+/)) {
                    return false;
            }

            pass_new = pass.split("").map(Number);
            //get every digit 
            pass_new.splice(2, 1);
            pass_new.splice(9, 1);
            //remove 3rd and 10th digit
            sum = pass_new.reduce((a, c) => a + c)
            //sum over all digits
            console.log(sum);
            //the sum of all digits is multiplied with the initial integer representaion of the value given
            console.log(sum * parseInt(pass));
            
            return (pass.length == 12 && sum * parseInt(pass) == 49157593271891 && pass_new[0] == 9)
    }
    

    document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('submit-button').onclick = () => {
                    if (is_valid_password(document.getElementById('input_form').value)) {
                            document.getElementById('result-text').innerHTML = '<span class="green">you got it! ❤ (ɔˆз(ˆ⌣ˆc)<br>your flag is </span><span class="yellow">flag{<span id="val" class="yellow">' + document.getElementById('input_form').value + '}</span> (◕‿◕)♡</span>'
                    } else {
                            document.getElementById('result-text').innerHTML = '<span id="val" class="yellow">' + document.getElementById('input_form').value + '</span> <span class="red">is wrong (‡▼益▼)</span>'
                    }

                    document.getElementById("val").textContent = document.getElementById('input_form').value;
            };
    });
}