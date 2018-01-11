import React, { Component } from 'react';
import styles from './../styles/PurchaseHistory.css';
import Purchase from './Purchase.js';

class PurchaseHistory extends Component {
  render() {

	  let purchaseHistory;
	  if(this.props.purchases) {
	  	purchaseHistory = this.props.purchases.map(purchase => {
	  		//console.log(project);
			return(
				<Purchase key={purchase.title} purchase={purchase} />
			);
	  	});
	  }


    return (
		<div>
			<h3>Your Payment History</h3>
	      	<table className='table'>
				<tbody>
					<tr>
				  		<th>Date</th>
						<th>Vendor</th>
						<th>Amount</th>
					</tr>
				</tbody>
				{purchaseHistory}
	  		</table>
		</div>
    );
  }
}

export default PurchaseHistory;
