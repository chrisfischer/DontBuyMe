import React, { Component } from 'react';

class Purchase extends Component {

// Everything needs to be inside the "App" div
  render() {
    return (
		<tbody>
		      <tr className="Purchase">
		        <td>{this.props.purchase.date}</td>
				<td>{this.props.purchase.vendor}</td>
				<td>{this.props.purchase.price}</td>
		      </tr>
		</tbody>
    );
  }
}

export default Purchase;
