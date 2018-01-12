import React from 'react'
import { Bar } from 'react-chartjs-2'

class Graph extends React.Component {

	constructor(props) {
		super(props)
	}

	render() {
		return (
			<div className='graph-container'>
				<div className="panel panel-default">
					<div className="panel-heading"><h5>Graph Title</h5></div>
					<Bar data={['1', '2', '3']} width={400} height={400}/>
				</div>
			</div>
		)
	}
}

export default Graph
