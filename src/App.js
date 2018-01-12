import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './Components/Header';
import Graph from './Components/Graph'
import PaymentHistory from './Components/PurchaseHistory';
import $ from 'jquery';


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
    }

    render() {
  	  console.log(this.state.data);
  	  return (
  		<div className="App">
  		  <Header />
  		  <Graph />
  		  <PaymentHistory purchases={this.state.purchases}/>
  		</div>
  	  );
    }
}

export default App;
