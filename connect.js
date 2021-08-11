function cmdoutput(cnt) {
  var i = document.getElementById("txtInput" + cnt).value;
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://192.168.99.101/cgi-bin/CGI.py?x=" + i, true);
  xhr.send();


  var inf = document.getElementById("txtInput" + cnt);
  inf.setAttribute("value", i);
  inf.innerHTML = "Value = " + "'" + i + "'";
  document.getElementById("txtInput" + cnt).disabled = true;

  xhr.onload = function () {
    var output = xhr.responseText;
    document.getElementById("result" + cnt).innerHTML = output;
  };
}
