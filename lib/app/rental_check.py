import streamlit as st


def deploy_streamlit(pipeline_output):
    """
    Deploys the Rental Check output to a Streamlit interface with an interactive format.

    Args:
        pipeline_output (Answers): The structured output from the LLM pipeline.

    Raises:
        ValueError: If pipeline_output is not in the expected format.
    """
    # Validate pipeline_output
    if not hasattr(pipeline_output, "renters") or not hasattr(
        pipeline_output, "letting_agency"
    ):
        raise ValueError("Pipeline output is not in the expected format.")

    # Renters
    if pipeline_output.renters.names:
        for name in pipeline_output.renters.names:
            with st.expander(f"**Renter Name:** {name.name.value}"):
                st.caption(f"Citation: {name.name.citation}")
    else:
        st.write("No renters found.")

    # Letting Agency
    if pipeline_output.letting_agency:
        with st.expander(f"**Agency Name:** {pipeline_output.letting_agency.value}"):
            st.caption(f"Citation: {pipeline_output.letting_agency.citation}")
    else:
        st.write("No letting agency found.")

    # Property Address
    if pipeline_output.property_address:
        with st.expander(f"**Address:** {pipeline_output.property_address.value}"):
            st.caption(f"Citation: {pipeline_output.property_address.citation}")
    else:
        st.write("No property address found.")

    # Agreement Date
    # TODO: if all None -> trigger else
    if pipeline_output.agreement_date:
        formatted_date = (
            f"{pipeline_output.agreement_date.day}/"
            f"{pipeline_output.agreement_date.month}/"
            f"{pipeline_output.agreement_date.year}"
        )
        with st.expander(f"**Agreement Date:** {formatted_date}"):
            st.caption(f"Citation: {pipeline_output.agreement_date.citation}")
    else:
        st.write("No agreement date found.")

    # Deposit
    if pipeline_output.deposit:
        deposit = f"{pipeline_output.deposit.amount} {pipeline_output.deposit.currency}"
        with st.expander(f"**Deposit:** {deposit}"):
            st.caption(f"Citation: {pipeline_output.deposit.citation}")
    else:
        st.write("No deposit information found.")

    # Rent
    if pipeline_output.rent:
        rent = f"{pipeline_output.rent.amount} {pipeline_output.rent.currency}"
        with st.expander(f"**Rent:** {rent}"):
            st.caption(f"Citation: {pipeline_output.rent.citation}")
    else:
        st.write("No rent information found.")
