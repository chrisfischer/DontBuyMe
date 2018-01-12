//
//  ViewController.swift
//  DontBuyMe
//
//  Created by Chris Fischer on 1/12/18.
//  Copyright © 2018 Chris Fischer. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var trueCostLabel: UILabel!
    @IBOutlet weak var interestCostLabel: UILabel!
    @IBOutlet weak var stockGainLabel: UILabel!
    
    @IBOutlet weak var costField: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        costField.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @objc func textFieldDidChange(_ textField: UITextField) {
        let price = costField.text
        if let price = price {
            var request = URLRequest(url: URL(string: "https://nessie-credit.herokuapp.com/api?key=896c897b5f52485fd3e9b049b4af1cc5&account=5a5796596514d52c7774a389&value=realCost&price=\(price)&time_reference=30")!)
            request.httpMethod = "GET"
            let session = URLSession.shared
            session.dataTask(with: request) { data, response, error in
                if (error != nil){
                    print("error")
                } else {
                    do {
                        let json = try JSONSerialization.jsonObject(with: data!, options:.allowFragments) as! [String : Double]
                        if let realCost = json["realCost"], let interestCost = json["interestCost"], let stockGain = json["investmentReturn"] {
                            DispatchQueue.main.async {
                                // now update UI on main thread
                                self.trueCostLabel.isHidden = false
                                self.stockGainLabel.isHidden = false
                                self.interestCostLabel.isHidden = false
                                self.trueCostLabel.text = String(format:"%.2f", realCost)
                                self.stockGainLabel.text = String(format:"%.2f", stockGain)
                                self.interestCostLabel.text = String(format:"%.2f", interestCost)
                            }
                        }
                    } catch {
                        print("Error")
                    }
                }
                }.resume()
        }
    }
}

