CREATE VIEW combined_energy_data AS
SELECT 
    gen.*,
    bio.biofuel_consumption, bio.biofuel_electricity, bio.biofuel_share_elec, bio.biofuel_share_energy,
    coa.coal_consumption, coa.coal_electricity, coa.coal_production, coa.coal_share_elec, coa.coal_share_energy,
    gas.gas_consumption, gas.gas_electricity, gas.gas_production, gas.gas_share_elec, gas.gas_share_energy,
    oil.oil_consumption, oil.oil_electricity, oil.oil_production, oil.oil_share_elec, oil.oil_share_energy,
    foss.fossil_electricity, foss.fossil_fuel_consumption, foss.fossil_share_elec, foss.fossil_share_energy, foss.carbon_intensity_elec,
    ghg.greenhouse_gas_emissions,
    hydr.hydro_consumption, hydr.hydro_electricity, hydr.hydro_share_elec, hydr.hydro_share_energy,
    nuc.nuclear_consumption, nuc.nuclear_electricity, nuc.nuclear_share_elec, nuc.nuclear_share_energy,
    rene.renewables_consumption, rene.renewables_electricity, rene.renewables_share_elec, rene.renewables_share_energy,
    sol.solar_consumption, sol.solar_electricity, sol.solar_share_elec, sol.solar_share_energy,
    win.wind_consumption, win.wind_electricity, win.wind_share_elec, win.wind_share_energy,
    oth.other_renewable_consumption, oth.other_renewable_electricity, oth.other_renewable_exc_biofuel_electricity, oth.other_renewables_share_elec, oth.other_renewables_share_elec_exc_biofuel, oth.other_renewables_share_energy,
    lowc.low_carbon_consumption, lowc.low_carbon_electricity, lowc.low_carbon_share_elec, lowc.low_carbon_share_energy,
    elec_imports.net_elec_imports, elec_imports.net_elec_imports_share_demand
FROM 
    general gen
INNER JOIN biofuel bio ON gen.country = bio.country AND gen.year = bio.year AND gen.iso_code = bio.iso_code
INNER JOIN coal coa ON gen.country = coa.country AND gen.year = coa.year AND gen.iso_code = coa.iso_code
INNER JOIN gas ON gen.country = gas.country AND gen.year = gas.year AND gen.iso_code = gas.iso_code
INNER JOIN oil ON gen.country = oil.country AND gen.year = oil.year AND gen.iso_code = oil.iso_code
INNER JOIN fossil foss ON gen.country = foss.country AND gen.year = foss.year AND gen.iso_code = foss.iso_code
INNER JOIN greenhouse_gas ghg ON gen.country = ghg.country AND gen.year = ghg.year AND gen.iso_code = ghg.iso_code
INNER JOIN hydro hydr ON gen.country = hydr.country AND gen.year = hydr.year AND gen.iso_code = hydr.iso_code
INNER JOIN nuclear nuc ON gen.country = nuc.country AND gen.year = nuc.year AND gen.iso_code = nuc.iso_code
INNER JOIN renewables rene ON gen.country = rene.country AND gen.year = rene.year AND gen.iso_code = rene.iso_code
INNER JOIN solar sol ON gen.country = sol.country AND gen.year = sol.year AND gen.iso_code = sol.iso_code
INNER JOIN wind win ON gen.country = win.country AND gen.year = win.year AND gen.iso_code = win.iso_code
INNER JOIN other_renewables oth ON gen.country = oth.country AND gen.year = oth.year AND gen.iso_code = oth.iso_code
INNER JOIN low_carbon lowc ON gen.country = lowc.country AND gen.year = lowc.year AND gen.iso_code = lowc.iso_code
INNER JOIN electricity_imports elec_imports  ON gen.country = elec_imports.country AND gen.year = elec_imports.year AND gen.iso_code = elec_imports.iso_code;
