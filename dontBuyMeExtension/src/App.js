import React, { Component } from 'react';
import Header from './Components/Header';
import PaymentHistory from './Components/PurchaseHistory';
import './App.css';
import uuid from 'uuid';

class App extends Component {
	constructor() {
		// set states here, pass from top down to other components
		super();
		this.state = {
			purchases: [],
		}
	}

	getPurchases() {
		this.setState(
			{
				purchases: [
					{
			  	    	'date': '2017-12-04',
						'id': '1234',
			  	        'vendor': 'STARBUCKS',
			  	        'price': '21.12'
			  	    },
					{
			  	   		'date': '2017-12-04',
						'id': '1235',
			  	        'vendor': 'GREENBURG MULTIPLEX',
			  	        'price': '13.23'
			  	    },
					{
			  	    	'date': '2017-12-06',
						'id': '1236',
			  	        'vendor': 'UBER',
			  	        'price': '54.40'
			  	    },
					{
			  	    	'date': '2017-12-12',
						'id': '1237',
			  	        'vendor': 'AMAZON.COM',
			  	        'price': '120.64'
			  	    },
					{
			  	    	'date': '2017-12-14',
						'id': '1238',
			  	        'vendor': 'NETFLIX',
			  	        'price': '9.99'
			  	    },
					{
			  	    	'date': '2017-12-16',
						'id': '1239',
			  	        'vendor': 'KAPNOS TAVERNA',
			  	        'price': '98.39'
			  	    }
				]
			}
		);
	}

	componentWillMount() {
		this.getPurchases();
	}

	render() {
		console.log(this.state.purchases);
	    return (
	      <div className="App">
	        <Header />
			<PaymentHistory purchases={this.state.purchases}/>
	      </div>
	    );
  	}
}

export default App;
