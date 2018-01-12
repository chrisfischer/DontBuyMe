import React, { Component } from 'react';
//import styles from './../styles/PurchaseHistory.css';
import Purchase from './Purchase.js';

class PurchaseHistory extends Component {
  render() {

	  let purchaseHistory;
	  if(this.props.purchases) {
	  	purchaseHistory = this.props.purchases.map(purchase => {
			return(
				<Purchase key={purchase.title} purchase={purchase} />
			);
	  	});
	  }


    return (
		<div className="purchaseHistory-container">
			<div className="panel panel-default">
				<div className="panel-heading"><h5>Your Payment History</h5></div>
		      	<div className="panel-body hold-height">
					<div className="list-group">
					{purchaseHistory}
					</div>
				</div>
			</div>
		</div>
    );
  }
}

export default PurchaseHistory;
