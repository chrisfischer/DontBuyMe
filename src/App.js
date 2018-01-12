import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './Components/Header';
import Graph from './Components/Graph'
import PaymentHistory from './Components/PurchaseHistory';
import $ from 'jquery';
import 'flexboxgrid'
import './styles/bootstrap/css/bootstrap.min.css'

class App extends Component {
	constructor() {
  	  // set states here, pass from top down to other components
  	  super();
  	  this.state = {
  		  purchases: [],
  		  data:[],
  		  options:[],
  	  }

    }

	getMonthlyCosts() {
		var xhr = new XMLHttpRequest();
		for (var month = 0; month < 12; month++) {
			xhr.open(
				"GET",
				"https://nessie-credit.herokuapp.com/api?key=896c897b5f52485fd3e9b049b4af1cc5&account=5a5796596514d52c7774a389&value=realMonthlyCostLoss&month=2017-" + (month+1),
				true
			);
			xhr.onreadystatechange = () => {
			  if (xhr.readyState == 4) {
				// JSON.parse does not evaluate the attacker's scripts.
				var resp = JSON.parse(xhr.responseText);
				console.log(resp);
			  }
			}
		}

		xhr.send();
	}

    getPurchases() {
  	  var xhr = new XMLHttpRequest();
  	  xhr.open(
		  "GET",
		  "https://nessie-credit.herokuapp.com/api?key=896c897b5f52485fd3e9b049b4af1cc5&account=5a5796596514d52c7774a389&value=purchaseHistory",
		  true
	  );
  	  xhr.onreadystatechange = () => {
  		if (xhr.readyState == 4) {
  		  // JSON.parse does not evaluate the attacker's scripts.
  		  var resp = JSON.parse(xhr.responseText);
  		  this.setState({purchases: resp});
  		}
  	  }
  	  xhr.send();
    }

    componentWillMount() {
  	  this.getPurchases();
	  this.getMonthlyCosts();
    }

    render() {
  	  return (
  		<div className="App">
		  <div id='app-container' className='row'>
		  	<Header />
			<div>
	  		  	<Graph className="panel"/>
			</div>
			<div>
	  		  <PaymentHistory purchases={this.state.purchases}/>
			</div>
		   </div>
  		</div>
  	  );
    }
}

export default App;
