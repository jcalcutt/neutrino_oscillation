**Python App:**

The idea behind this RESTFUL Flask API is to provide probabilities of neutrino oscillations, given some initial conditions. For example, what’s the probability you will observe a different flavour of neutrino 500km away which has an energy of 5 GeV.

**Some Context:**

Neutrinos are fundamental particles of the standard model. They are extremely small, but as numerous experiments have reported over the last couple of decades - not completely massless. This is a slight, but significant divergence as to what the standard model predicts.

Our current understanding is that neutrinos exist in 3 lepton flavours: electron, muon and tau. One of their most interesting properties, is their ability to ‘transform’ flavours as they propagate through space and time. So for example, for a given energy, we can observe a mono-energetic beam of muon neutrinos at point x. However, if we measure the same beam at point y, there is a finite probability some of the muon neutrinos will have ‘transformed’ to electron neutrinos. This phenomenon is referred to as neutrino oscillation and, although predicted 60 years ago, has been a hotbed of active research over the last 20 years. It’s this oscillation behaviour that, ultimately, allows scientists to indirectly infer their non-zero mass.

For Two Phase oscillation, the probability of oscillation is governed by the equation:

 ![EQUATION](https://latex.codecogs.com/gif.latex?P_%7Ba%5Crightarrow%20b%7D%20%3D%20sin%5E2%282%5CTheta%20%29sin%5E2%281.27%5Ccdot%20%28%5CDelta%20m%5E2_%7B21%7DL/%20E%29%29)

*where: &Theta; is the mixing angle, &Delta;m is the mass difference between neutrino flavours, L is the distance travelled by the neutrino (in km), and E is the energy of the neutrino (in GeV)*



**API:**

Swagger docs here:

[swagger.yaml](swagger.yaml)

**To Run:**

To run locally:

*requires python 3.7*

`>python application.py`